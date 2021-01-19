public class Main extends Thread {
    public static void main(String[] args) {
        new Main().start();
        new Main().start();
    }
    public void run() {
        System.out.println(Thread.currentThread().getName() + ":" + MySystem.getInstance().getDate());
    }
}
