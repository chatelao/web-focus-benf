Appendix B

Error Messages

To see the text or explanation for any error message, you can display it or find it in an
errors file. All of the FOCUS error messages are stored in eight system ERRORS files.

For UNIX, Windows, and Open/VMS, the extension is .err.

For z/OS, the ddname is ERRORS.

In this appendix:

Displaying Messages

Displaying Messages

To display the text and explanation for any message, issue the following query command in a
stored procedure

? n

where:

n

Is the message number.

The message number and text appear, along with a detailed explanation of the message (if
one exists). For example, issuing the following command

? 210

displays the following:

(FOC210)    THE DATA VALUE HAS A FORMAT ERROR:
An alphabetic character has been found where all numerical digits are
required.

Describing Data With TIBCO WebFOCUS® Language

 517

Displaying Messages

518
