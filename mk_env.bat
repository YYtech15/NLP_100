@echo off
setlocal

rem �f�B���N�g�����X�g���`
set directories="01_�����^��" "02_UNIX�R�}���h" "03_���K�\��" "04_�`�ԑf���" "05_�W��󂯉��" "06_�@�B�w�K" "07_�P��x�N�g��" "08_�j���[�����l�b�g" "09_RNN_CNN" "10_�@�B�|��"

rem �e�f�B���N�g�����쐬���A1.py����10.py���쐬
for %%d in (%directories%) do (
    if not exist %%d (
        mkdir %%d
        echo Directory %%d created.
    )
    for /l %%i in (1,1,10) do (
        echo # %%i.py > "%%d/%%i.py"
        echo File %%i.py created in %%d.
    )
)

echo All directories and Python files created successfully.
pause