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
        FreezeJson4Holder holder0 = new FreezeJson4Holder(docstr);
        ObjectOutputStream oos = new ObjectOutputStream
            (new FileOutputStream(new File("test.bin")));
        oos.writeObject(holder0);
        oos.close();

        ObjectInputStream ois = new ObjectInputStream
            (new FileInputStream(new File("test.bin")));
        FreezeJson4Holder holder1 = (FreezeJson4Holder)ois.readObject();
        ois.close();

        System.out.printf("BodySize1 = %d, BodySize2 = %d\n",
                          holder0.BodySize(), holder1.BodySize());
    }
}
