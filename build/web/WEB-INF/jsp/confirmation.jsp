<%-- 
    Document   : confirmation
    Created on : Jun 23, 2019, 6:09:06 PM
    Author     : User
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>You entered following data:</h1>
        <p>First name: ${first_name}</p>
        <p>Last name: ${last_name}</p>
        <p>Date of birth: ${date_of_birth}</p>
        <p>Personal ID number: ${pid}</p>
        <p>Email: ${email}</p>
        <p>Country: ${country}</p>
        <p>City ${city}</p>
        <p>Postal ${postal}</p>
    </body>
</html>
