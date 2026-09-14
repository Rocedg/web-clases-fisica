$ErrorActionPreference = 'Stop'
$lessonRepo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
New-Item -ItemType Directory -Path (Join-Path $lessonRepo 'tmp/lesson-review') -Force | Out-Null
Push-Location (Join-Path $lessonRepo 'content/lessons/latex')
try {
    foreach ($lesson in Get-ChildItem 'T[0-6]-*.tex') {
        foreach ($pass in 1..3) {
            $buildOutput = & pdflatex '-interaction=nonstopmode' '-halt-on-error' '-output-directory=../../../tmp/lesson-review' $lesson.Name 2>&1
            if ($LASTEXITCODE -ne 0) {
                $buildOutput | Select-Object -Last 22
                throw "Compilation failed: $($lesson.Name)"
            }
        }
        $buildOutput | Select-String 'Output written|Overfull|Underfull|undefined'
    }
} finally {
    Pop-Location
}
