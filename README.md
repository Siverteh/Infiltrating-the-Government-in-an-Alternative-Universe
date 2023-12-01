# Infiltrating-the-Government-in-an-Alternative-Universe
Assignment 4 - Infiltrating the Government in an Alternative Universe
First and foremost
Here are some guidelines on what not to do during this assignment:

Spamming: Do not send excessive, irrelevant, or inappropriate messages or requests. This includes overloading the server with heavy traffic, sending repeated requests, or flooding the chat.

Destructive Behavior: Do not engage in any activities that could harm the systems you are working with, such as introducing malware, deleting files or databases, or disrupting services.

Illegal Activities: Do not engage in any illegal activities. This includes hacking into unauthorized areas, stealing data, violating privacy laws, or any other actions that are against the law.

Unethical Actions: Do not use the information gained during this assignment for unethical purposes. This includes blackmail, defamation, spreading false information, or any other actions that could harm individuals or organizations.

Violation of Privacy: Respect all forms of privacy. Do not attempt to access personal information about individuals without their explicit consent.

Harassment: Do not use any form of harassment or offensive language.

Plagiarism: All work submitted should be your own. Do not copy others' work without proper attribution.
Remember, the goal of this assignment is to learn and develop your skills in a safe and ethical manner. Clearly, you are no wizard if you mess up this.

Description
In this assignment, you will be exploring the internet from an alternative universe. The Norwegian Government in this universe has stored state secrets about recent incidents that have been revealed through the media. Your task is to identify vulnerabilities in their systems and use them to gain access to these state secrets, which are rumored to be stored in a binary email database.

There are many potential vulnerabilities to exploit, including side-channel vulnerabilities, buffer overflow vulnerable code, and XSS.

Your journey begins here: https://regjeringen.uiaikt.no/Links to an external site. and https://github.com/uiaict/2023-ikt222-templateLinks to an external site.

 

Remember to document the information you find along the way. Use LaTeX to explain your findings. The final task is to reverse engineer the state secrets.

All tasks should be solvable using Python. It is recommended to use poetry for this task. The recommended structure of your project is as follows:

code
   solutions
       attack_1
           main.py
           <other files needed (should be run with main.py)>
   pyproject.toml
   poetry.lock
   readme.md

Hints
Vulnerable Function Used to Evaluate Password
The following function is used to evaluate passwords in some parts of the system:

int total_time = 0;

if (a.length() != b.length()) {
    return total_time;
}

for (size_t i = 0; i <= a.length(); ++i) {
    if (a[i] != b[i]) {
        return total_time;
    }
    total_time++;
}
return total_time;

Intranet: Level 1
Jonas Dahl frequently logs in to check his Wireguard credentials.
Discord WEBHOOKS can be very useful here.
Consider using the webhook to send data to yourself when Jonas Dahl logs in.
Keep an eye out for information about Jonas' supervisor. She might have more access than Jonas.
Intranet: Level 2
You need to access the network on Wireguard. You'll retrieve this on Intranet: Level 1.
nmap is a great tool for service discovery. Perhaps you can check which ports are open?
SSH
The SSH Server only accepts public-key authentication. You need to do something before accessing this server. What if we could overwrite the authorized_keys file somehow?
Use ssh-rsa keys.
Dropbox
Consider how Dropbox could be used to gain access to SSH.