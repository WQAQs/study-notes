public class Main {
    public static void main(String[] args) {
        System.out.println("main: BEGIN");
        try {
            // 啟動執行緒
            HanoiThread t = new HanoiThread();
            t.start();

            // 等待一段時間
            Thread.sleep(10000);

            // 對執行緒送出終止請求
            System.out.println("main: shutdownRequest");
            t.shutdownRequest();

            // 等待執行緒集結束
            System.out.println("main: join");
            t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("main: END");
    }
}
