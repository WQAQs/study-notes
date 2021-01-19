public class Bank {
    private int money;
    private String name;

    public Bank(String name, int money) {
        this.name = name;
        this.money = money;
    }

    // �s���
    public synchronized void deposit(int m) {
        money += m;
    }

    // ȡ��
    public synchronized boolean withdraw(int m) {
        if (money >= m) {
            money -= m;
            return true;    // �w��ȡ��
        } else {
            return false;   // ����
        }
    }

    public String getName() {
        return name;
    }
}
