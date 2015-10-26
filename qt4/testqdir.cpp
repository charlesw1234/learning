#include <QDir>

int
main(void)
{
    QDir dobj(".");
    foreach (QString entry,
             dobj.entryList(QStringList("*.cpp"), QDir::Files, QDir::Name))
        printf("%s\n", entry.toUtf8().constData());
    QString fpath(dobj.filePath("../../learning/pyqt/tsplitter.py"));
    printf("fpath: %s\n", fpath.toUtf8().constData());
    return 0;
}
