public class Main {
    public static void main(String[] args) {
        Channel channel = new Channel(5);   // 工人线程的數量
        channel.startWorkers();
        new ClientThread("Alice", channel).start();
        new ClientThread("Bobby", channel).start();
        new ClientThread("Chris", channel).start();
    }
}
