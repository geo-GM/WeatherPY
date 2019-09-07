/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.time.LocalDate;
import javax.validation.constraints.NotNull;
import org.hibernate.validator.constraints.Email;
import org.hibernate.validator.constraints.NotEmpty;
import org.springframework.format.annotation.DateTimeFormat;

/**
 *
 * @author User
 */
public class User {
    @NotEmpty
    private String first_name;
    
    @NotEmpty
    private String last_name;
    
    @NotNull
  @DateTimeFormat(iso = DateTimeFormat.ISO.DATE)
    private LocalDate date_of_birth;
    
    @NotEmpty
    private String pid;
    
    @Email
    @NotEmpty
    private String email;

    @NotEmpty    
    private String country;
    
    @NotEmpty
    private String city;
    
    @NotEmpty
    private String postal;

    public String getFirst_name() {
        return first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public LocalDate getDate_of_birth() {
        return date_of_birth;
    }

    public String getPid() {
        return pid;
    }

    public String getEmail() {
        return email;
    }

    public String getCountry() {
        return country;
    }

    public String getCity() {
        return city;
    }

    public String getPostal() {
        return postal;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public void setDate_of_birth(LocalDate date_of_birth) {
        this.date_of_birth = date_of_birth;
    }

    public void setPid(String pid) {
        this.pid = pid;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setPostal(String postal) {
        this.postal = postal;
    }      
}
