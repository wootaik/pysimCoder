void sendMsg(WORD ID, BYTE DATA[], int len);
int rcvMsg(BYTE DATA[], int timeout);
int rcvMsgCob(int cob, BYTE DATA[], int timeout);
int canOpen();
int canOpenTH();
void canClose();
void canopen_synch();
int registerMsg(int ID, WORD index, BYTE subindex);
int getValue(int ID, WORD index, BYTE subindex);
short get2ByteValue(int ID, WORD index, BYTE subindex);
