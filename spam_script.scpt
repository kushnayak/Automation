# sendMessage.scpt
on run {targetPhoneNumber, targetMessageToSend}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetPhoneNumber of targetService
        set targetMessage to targetMessageToSend
--        say targetMessage
        send targetMessage to targetBuddy
    end tell
end run

--tell application "Messages"
--	set textbuddy to buddy "+19256391311" of service id "C34FC328-39CF-471D-AC2B-F2DC6A2F8D6F"
--	send "lmao this actually worked" to textbuddy
--end tell