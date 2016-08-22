package com.wl.www;

import java.io.IOException;
import java.io.Serializable;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Person1 implements Serializable {
    private static final long serialVersionUID = 1L;

    private int age;
    public int get_age() { return age; }
    public void set_age(int age) { this.age = age; }

    private void writeObject(ObjectOutputStream stream) throws IOException {
        stream.write(65);
        stream.write(age);
        stream.write(66);
    }
    private void readObject(ObjectInputStream stream) throws IOException {
        stream.read();
        age = stream.read();
        stream.read();
    }
}
