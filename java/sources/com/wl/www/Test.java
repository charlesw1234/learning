package com.wl.www;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Test {
    public static void main(String args[]) throws Exception {
        FileInputStream fis = new FileInputStream(new File("test.json"));
        byte[] fbody = new byte[4096];
        int fbodylen = fis.read(fbody);
        fis.close();

        String docstr = new String(fbody, 0, fbodylen, "UTF-8");
        FreezeJson4 doc0 = new FreezeJson4(docstr);
        ObjectOutputStream oos = new ObjectOutputStream
            (new FileOutputStream(new File("test.bin")));
        oos.writeObject(doc0);
        oos.close();

        System.out.printf("Root Object Size = %d\n", doc0.GetObjectSize(0));

        ObjectInputStream ois = new ObjectInputStream
            (new FileInputStream(new File("test.bin")));
        FreezeJson4 doc1 = (FreezeJson4)ois.readObject();
        ois.close();

        System.out.printf("BodySize1 = %d, BodySize2 = %d\n", doc0.BodySize(), doc1.BodySize());
    }
}
