"""Corrige o clique no mapa do Yume quando ele roda no Switch (Carafe/Autorun).

Antes de aceitar um clique, o Frog.exe confere se a janela sob o cursor é a dele
(WindowFromPoint). No Switch o Autorun desenha o cursor por cima, essa conferência
falha e o clique é descartado: a fase fica selecionada, mas não entra.
O patch troca 6 bytes (um salto condicional em 0x4415A0) por NOPs. No PC não muda nada.

uso: python patch_frog.py "caminho\\para\\Frog.exe"
(cria Frog.exe.original como backup)
"""
import hashlib, shutil, sys

ORIGINAL_MD5 = "0669beacbc15649a62edf16f6101233f"
OFFSET = 0x415A0
EXPECTED = bytes.fromhex("0f85b3000000")
PATCHED = b"\x90" * 6

path = sys.argv[1] if len(sys.argv) > 1 else "Frog.exe"
data = bytearray(open(path, "rb").read())
if data[OFFSET:OFFSET + 6] == PATCHED:
    sys.exit("Este Frog.exe já está corrigido.")
if hashlib.md5(data).hexdigest() != ORIGINAL_MD5 or data[OFFSET:OFFSET + 6] != EXPECTED:
    sys.exit("Este Frog.exe é de outra versão. Nada foi alterado.")
shutil.copyfile(path, path + ".original")
data[OFFSET:OFFSET + 6] = PATCHED
open(path, "wb").write(data)
print("Pronto. Backup salvo em", path + ".original")
