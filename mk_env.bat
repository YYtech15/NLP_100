@echo off
setlocal

rem ディレクトリリストを定義
set directories="01_準備運動" "02_UNIXコマンド" "03_正規表現" "04_形態素解析" "05_係り受け解析" "06_機械学習" "07_単語ベクトル" "08_ニューラルネット" "09_RNN_CNN" "10_機械翻訳"

rem 各ディレクトリを作成し、1.pyから10.pyを作成
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