
TITLE - ProvUpgifft

msg "%username%" This is a test!


@echo off
cd %USERPROFILE%\Desktop
md WebSite
cd WebSite
md Application1
md Application2
md Application3
echo Hello, this is a file. > Application1\st.txt
echo Hello, this is a file. > Application1\mt.docx
echo Hello, this is a file. > Application3\Page1.htm
echo Hello, this is a file. > Application3\Page2.htm
cd Application3
md Media

