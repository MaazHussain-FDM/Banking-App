param(
    [Parameter(Mandatory = $true)]
    [string]$NssmPath,
    [string]$ServiceName = "DjangoBankingApp",
    [string]$AppDirectory = (Get-Location).Path,
    [string]$Host = "0.0.0.0",
    [int]$Port = 8000
)

$pythonPath = (Get-Command python).Source
$arguments = "-m waitress --listen=$Host`:$Port banking_project.wsgi:application"

& $NssmPath install $ServiceName $pythonPath $arguments
& $NssmPath set $ServiceName AppDirectory $AppDirectory
& $NssmPath set $ServiceName AppStdout (Join-Path $AppDirectory "service.out.log")
& $NssmPath set $ServiceName AppStderr (Join-Path $AppDirectory "service.err.log")
& $NssmPath start $ServiceName

