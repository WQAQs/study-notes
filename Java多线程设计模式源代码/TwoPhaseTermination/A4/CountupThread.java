public class CountupThread extends GracefulThread {
    // 计数器的值
    private long counter = 0;

    
    protected void doWork() throws InterruptedException {
        counter++;
        System.out.println("doWork: counter = " + counter);
        Thread.sleep(500);
    }

   
    protected void doShutdown() {
        System.out.println("doShutdown: counter = " + counter);
    }
}
