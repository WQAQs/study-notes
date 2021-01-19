package readwritelock;

public class Data {
    private final ReadWriteLock lock;
    private final ReadWriteStrategy readWriteStrategy;
    public Data() {
        this.lock = new ReadWriteLock(new DefaultGuardStrategy());
        this.readWriteStrategy = new DefaultReadWriteStrategy();
    }
    public Data(GuardStrategy guardStrategy) {
         this.lock = new ReadWriteLock(guardStrategy);
        this.readWriteStrategy = new DefaultReadWriteStrategy();
    }
    public Data(ReadWriteStrategy readWriteStrategy) {
        this.lock = new ReadWriteLock(new DefaultGuardStrategy());
         this.readWriteStrategy = readWriteStrategy;
    }
    public Data(GuardStrategy guardStrategy, ReadWriteStrategy readWriteStrategy) {
         this.lock = new ReadWriteLock(guardStrategy);
         this.readWriteStrategy = readWriteStrategy;
    }
    public Object read() throws InterruptedException {
        lock.readLock();
        try {
            return readWriteStrategy.doRead();
        } finally {
            lock.readUnlock();
        }
    }
    public void write(Object arg) throws InterruptedException {
        lock.writeLock();
        try {
            readWriteStrategy.doWrite(arg);
        } finally {
            lock.writeUnlock();
        }
    }

    // Inner class

    private class ReadWriteLock {
        private final GuardStrategy guardStrategy;
        public ReadWriteLock(GuardStrategy guardStrategy) {
            this.guardStrategy = guardStrategy;
        }
        public synchronized void readLock() throws InterruptedException {
            guardStrategy.beforeReadWait();
            try {
                while (!guardStrategy.readGuard()) {
                    wait();
                }
            } finally {
                guardStrategy.afterReadWait();
            }
            guardStrategy.beforeDoRead();
        }
        public synchronized void readUnlock() {
            guardStrategy.afterDoRead();
            notifyAll();
        }
        public synchronized void writeLock() throws InterruptedException {
            guardStrategy.beforeWriteWait();
            try {
                while (!guardStrategy.writeGuard()) {
                    wait();
                }
            } finally {
                guardStrategy.afterWriteWait();
            }
            guardStrategy.beforeDoWrite();
        }
        public synchronized void writeUnlock() {
            guardStrategy.afterDoWrite();
            notifyAll();
        }
    }

    // Inner class

    private class DefaultGuardStrategy implements GuardStrategy {
        private int readingReaders = 0; // ���ۂɓǂ�ł���X���b�h�̐�
        private int writingWriters = 0; // ���ۂɏ����Ă���X���b�h�̐�
        private int waitingWriters = 0; // �����̂�҂��Ă���X���b�h�̐�
        private boolean preferWriter = true; // �����̂�D�悷��Ȃ�true
        public void beforeReadWait() {
            // no operation
        }
        public boolean readGuard() {
            return !(writingWriters > 0 || (preferWriter && waitingWriters > 0));
        }
        public void afterReadWait() {
            // no operation
        }
        public void beforeDoRead() {
            readingReaders++;
        }
        public void afterDoRead() {
            readingReaders--;                      
            preferWriter = true;
        }
        public void beforeWriteWait() {
            waitingWriters++;
        }
        public boolean writeGuard() {
            return !(readingReaders > 0 || writingWriters > 0);
        }
        public void afterWriteWait() {
            waitingWriters--;
        }
        public void beforeDoWrite() {
            writingWriters++;
        }
        public void afterDoWrite() {
            writingWriters--;                       
            preferWriter = false;
        }
    }

    // Inner class

    private class DefaultReadWriteStrategy implements ReadWriteStrategy {
        private final char[] buffer;
        public DefaultReadWriteStrategy() {
            this(10);
        }
        public DefaultReadWriteStrategy(int size) {
            this.buffer = new char[size];
            for (int i = 0; i < buffer.length; i++) {
                buffer[i] = '*';
            }
        }
        public Object doRead() throws InterruptedException {
            char[] newbuf = new char[buffer.length];
            for (int i = 0; i < buffer.length; i++) {
                newbuf[i] = buffer[i];
            }
            slowly();
            return newbuf;
        }
        public void doWrite(Object arg) throws InterruptedException {
            char c = ((Character)arg).charValue();
            for (int i = 0; i < buffer.length; i++) {
                buffer[i] = c;
                slowly();
            }
        }
        private void slowly() throws InterruptedException {
            Thread.sleep(50);
        }
    }
}
