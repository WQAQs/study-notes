public class HanoiThread extends Thread {
    // 已經送出終止請求則為true
    private volatile boolean shutdownRequested = false;
    // 送出終止請求的時刻
    private volatile long requestedTimeMillis = 0;

    // 終止請求
    public void shutdownRequest() {
        requestedTimeMillis = System.currentTimeMillis();
        shutdownRequested = true;
        interrupt();
    }

    // 判斷終止請求是否已經送出
    public boolean isShutdownRequested() {
        return shutdownRequested;
    }

    // 動作
    public void run() {
        try {
            for (int level = 0; !shutdownRequested; level++) {
                System.out.println("==== Level " + level + " ====");
                doWork(level, 'A', 'B', 'C');
                System.out.println("");
            }
        } catch (InterruptedException e) {
        } finally {
            doShutdown();
        }
    }

    // 作業
    private void doWork(int level, char posA, char posB, char posC) throws InterruptedException {
        if (level > 0) {
            doWork(level - 1, posA, posC, posB);
            System.out.print(posA + "->" + posB + " ");
            doWork(level - 1, posC, posB, posA);
        }
    }

    // 終止處理
    private void doShutdown() {
        long time = System.currentTimeMillis() - requestedTimeMillis;
        System.out.println("doShutdown: Latency = " + time + " msec.");
    }
}
