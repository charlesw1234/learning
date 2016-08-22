package com.wl.www;

import java.io.Serializable;

public class Persons implements Serializable {
    private static final long serialVersionUID = 1L;

    private Person0 person0;
    public void set_age0(int age) {
        System.out.println("Persons.set_age0");
        person0.set_age(age);
    }

    private Person1 person1;
    public void set_age1(int age) {
        System.out.println("Persons.set_age1");
        person1.set_age(age);
    }

    public Persons() {
        System.out.println("Persons.Persons()");
        person0 = new Person0(); person1 = new Person1();
    }
}
