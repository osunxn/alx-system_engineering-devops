Postmortem:
ALX System Engineering & DevOps Project 0x19 Outage

Web Stack Debugging 3
In this project, we delve into debugging issues in a web stack, employing various tools and techniques to identify and resolve problems efficiently.

File Structure
0x17-web_stack_debugging_3/
├── 0-strace_is_your_friend.pp
└── README.md

Issue Summary
Duration: April 12, 2024, 10:00 AM - April 12, 2024, 11:30 AM (UTC-5)
Impact: WordPress site experienced a 500 error, rendering it inaccessible to users. Approximately 70% of users were affected.
Root Cause: Incorrect file extension (.phpp instead of .php) in wp-settings.php.

Timeline
10:00 AM: Issue detected through monitoring alert.
10:05 AM: Engineer initiated investigation, suspecting a configuration error.
10:15 AM: Initial assumption made about potential misconfiguration in Apache or PHP settings.
10:30 AM: After inspecting Apache and PHP configurations, no anomalies found.
10:45 AM: Misleading path taken, focusing on server memory utilization, leading to no relevant findings.
11:00 AM: Incident escalated to senior sysadmin for further assistance.
11:30 AM: Issue resolved by correcting file extension in wp-settings.php.

Root Cause and Resolution
The issue stemmed from an incorrect file extension (.phpp instead of .php) in the wp-settings.php file. This caused Apache to interpret the file incorrectly, resulting in the 500 error. The problem was resolved by using the sed command to replace the incorrect extension with the correct one.

Corrective and Preventative Measures
To prevent similar incidents in the future, the following actions will be taken:
Regular review of file configurations to catch any discrepancies.
Implementation of automated tests to validate configurations.
Training for team members on troubleshooting techniques.

Additional Notes
While postmortems serve as valuable learning experiences, the emphasis lies on proactive measures to prevent recurrences and foster a robust system.

Make people want to read your postmortem
To make the postmortem engaging, we could include a humorous anecdote related to debugging, a visually appealing diagram illustrating the debugging process, or even a fictional narrative to draw readers' attention.

URLs
[GitHub Repository: alx-system_engineering-devops 0-strace_is_your_friend.pp ](https://github.com/osunxn/alx-system_engineering-devops/blob/main/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp)
