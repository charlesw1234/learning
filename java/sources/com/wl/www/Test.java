package com.wl.www;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Test {
    public static void main(String args[]) throws Exception {
        Person0 person0 = new Person0();
        person0.set_age(16);
        Person1 person1 = new Person1();
        person1.set_age(17);
        Persons persons = new Persons();
        persons.set_age0(18);
        persons.set_age1(19);

        ObjectOutputStream oo0 = new ObjectOutputStream
            (new FileOutputStream(new File("test0.txt")));
        oo0.writeObject(person0);
        oo0.close();

        ObjectOutputStream oo1 = new ObjectOutputStream
            (new FileOutputStream(new File("test1.txt")));
        oo1.writeObject(person1);
        oo1.close();

        ObjectOutputStream oos = new ObjectOutputStream
            (new FileOutputStream(new File("tests.txt")));
        oos.writeObject(persons);
        oos.close();
    }
}
