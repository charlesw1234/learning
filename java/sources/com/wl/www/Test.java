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
        FreezeDocument4 doc0 = new FreezeDocument4(docstr);
        ObjectOutputStream oos = new ObjectOutputStream
            (new FileOutputStream(new File("test.bin")));
        oos.writeObject(doc0);
        oos.close();

        System.out.printf("Root Object Size = %d\n", doc0.GetObjectSize(0));

        ObjectInputStream ois = new ObjectInputStream
            (new FileInputStream(new File("test.bin")));
        FreezeDocument4 doc1 = (FreezeDocument4)ois.readObject();
        ois.close();

        System.out.printf("BodySize1 = %d, BodySize2 = %d\n", doc0.BodySize(), doc1.BodySize());
        System.out.printf("doc0(%s)\n", doc0.Render(0));
        recur_show("doc0:", doc0, 0);
        System.out.printf("doc1(%s)\n", doc1.Render(0));
        recur_show("doc1:", doc1, 0);
    }
    public static void recur_show(String indent, FreezeDocument4 doc, int pos)
    {
        if (doc.IsRemoved(pos)) System.out.printf("%sremoved\n", indent);
        if (doc.IsNull(pos)) System.out.printf("%snull\n", indent);
        else if (doc.IsFalse(pos)) System.out.printf("%sfalse\n", indent);
        else if (doc.IsTrue(pos)) System.out.printf("%strue\n", indent);
        else if (doc.IsInt(pos)) System.out.printf("%s%d\n", indent, doc.GetInt(pos));
        else if (doc.IsUint(pos)) System.out.printf("%s%d\n", indent, doc.GetUint(pos));
        else if (doc.IsDouble(pos)) System.out.printf("%s%f\n", indent, doc.GetDouble(pos));
        else if (doc.IsString(pos)) System.out.printf("%s%s\n", indent, doc.GetString(pos));
        else if (doc.IsArray(pos)) {
            System.out.printf("%s[\n", indent);
            for (int idx = 0; idx < doc.GetArraySpace(pos); ++idx)
                recur_show(indent + "    ", doc, doc.GetArray(pos, idx));
            System.out.printf("%s]\n", indent);
        } else if (doc.IsObject(pos)) {
            System.out.printf("%s{\n", indent);
            for (int idx = 0; idx < doc.GetObjectSpace(pos); ++idx) {
                System.out.printf("%s    \"%s\":\n", indent, doc.GetObjectKey(pos, idx));
                recur_show(indent + "   ", doc, doc.GetObject(pos, idx));
            }
            System.out.printf("%s}\n", indent);
        }
    }
}
