<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<!DOCTYPE html>

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>New User</title>

        <style>
            .field
            {
                clear:both;
                padding:5px;
            }

            .field label
            {
                text-align: left;
                width:100px;
                float:left;
            }

            .error
            {
                color: red;
            }

        </style>


    </head>

    <body>
        <form:form action="new_user.htm" method="post" commandName="user">

            <div class=" label ">
                <form:label path="first_name">First name</form:label>
                <form:input path="first_name" />
                <form:errors path="first_name" cssClass="error"></form:errors>
                </div>

                <div class="field">
                <form:label path="last_name">Last name</form:label>
                <form:input path="last_name" />
                <form:errors path="last_name" cssClass="error"></form:errors>
                </div>

                <div class="field">
                <form:label path="date_of_birth">Date of birth</form:label>
                <form:input path="date_of_birth" type="date" id="date_field"/>
                <form:errors path="date_of_birth" cssClass="error"></form:errors>
                </div>

                <div class="field">
                <form:label path="pid">Personal ID number</form:label>
                <form:input path="pid"/>
                <form:errors path="pid" cssClass="error"></form:errors>
                </div>

                <div class="field">
                <form:label path="email">Email</form:label>
                <form:input path="email" />
                <form:errors path="email" cssClass="error"></form:errors>
                </div>

                <div class="field">
                <form:label path="country">Country</form:label>
                <form:input path="country" />
                <form:errors path="country" cssClass="error"></form:errors>
                </div>

                <div class="field">
                <form:label path="city">City</form:label>
                <form:input path="city" />
                <form:errors path="city" cssClass="error"></form:errors>
                </div>

                <div class="field">
                <form:label path="postal">Postal code</form:label>
                <form:input path="postal" />
                <form:errors path="postal" cssClass="error"></form:errors>
                </div>

                <input type="submit" value="Submit"/>
        </form:form>
    </body>
</html>