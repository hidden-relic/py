#NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.
#Persistent

return

^#a::
	Loop
	{
		if GetKeyState("End")
			break
		; tt("Getting line..")
		s("{Home}", "{Shift Down}", "{End}", "{Shift Up}")
		; tt("saving old clipboard..", clipboard)
		old_cb:=clipboard
		; tt("cutting line to clipboard..")
		s("^x")
		line:=clipboard
		; tt("line cut", line)
		clipboard:=old_cb
		; tt("resetting clipboard and erasing whitespace..", clipboard)
		s("{Shift Down}", "{Home}", "{Shift Up}", "{Backspace}")
		if InStr(line, "def ")
		{
			; tt("function definition")
			s(line)
			Break
		}
		else
		{
			; tt("not func")
			S("{BackSpace}", "{Enter}", line, "{Down}")
		}
	}
return

s(x*){
	for a,b in x
	{
		Send, % b
		Sleep, 250
	}
}

tt(x*){
	tool:=""
	for a,b in x
		tool.=b "`n"
	ToolTip, % tool
	Sleep, 2000
	ToolTip
}
