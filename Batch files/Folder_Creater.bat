
TITLE - ProvUpgifft
echo Vill du skapa mappar och filer på din Desktop?
pause
"xcopy koipierar allt i mapparna"
cd %USERPROFILE%\Desktop
md MyFiles
cd MyFiles
md Images
md Documents
"md Application3"
"echo Hello, this is a file. > Application1\st.txt
"echo Hello, this is a file. > Application1\mt.docx
"echo Hello, this is a file. > Application3\Page1.htm
echo Hello, this is a file. > Documents\Messeges.txt
"cd     
"md Media
echo Done

pause 

msg "%username%" Filerna har nu skapats på ditt skrivbord!