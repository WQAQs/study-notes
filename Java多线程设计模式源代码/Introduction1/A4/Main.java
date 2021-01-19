public class Main {
    public static void main(String[] args) {
        Bank bank = new Bank("A Bad Bank", 1000);   
        new ClientThread(bank).start();
        new ClientThread(bank).start();
    }
}
