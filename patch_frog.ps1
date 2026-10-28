# Mesmo patch do patch_frog.py, para quem não tem Python (PowerShell já vem no Windows).
# uso: clique com o botão direito > "Executar com o PowerShell", ou:
#   powershell -ExecutionPolicy Bypass -File patch_frog.ps1 "C:\caminho\Yume\Frog.exe"
param([string]$Path = "Frog.exe")
$md5 = "0669BEACBC15649A62EDF16F6101233F"
$offset = 0x415A0
$expected = [byte[]](0x0F,0x85,0xB3,0x00,0x00,0x00)
$bytes = [System.IO.File]::ReadAllBytes((Resolve-Path $Path))
$slice = $bytes[$offset..($offset+5)]
if (($slice | Where-Object { $_ -ne 0x90 }).Count -eq 0) { Write-Host "Este Frog.exe ja esta corrigido."; exit }
$hash = (Get-FileHash -Algorithm MD5 $Path).Hash
if ($hash -ne $md5 -or (Compare-Object $slice $expected)) { Write-Host "Este Frog.exe e de outra versao. Nada foi alterado."; exit 1 }
Copy-Item $Path "$Path.original"
for ($i = 0; $i -lt 6; $i++) { $bytes[$offset + $i] = 0x90 }
[System.IO.File]::WriteAllBytes((Resolve-Path $Path), $bytes)
Write-Host "Pronto. Backup salvo em $Path.original"
