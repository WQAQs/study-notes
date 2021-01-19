public class Main {
    public static void main(String[] args) {
        System.out.println("main:BEGIN");

        // �趨shutdown hook
        Runtime.getRuntime().addShutdownHook(
            new Thread() {
                public void run() {
                    System.out.println("*****");
                    System.out.println(Thread.currentThread().getName() + ": SHUTDOWN HOOK!");
                    System.out.println("*****");
                }
            }
        );

        System.out.println("main:SLEEP...");

        // Լ3���ǿ�ƽ�������
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
        }

        System.out.println("main:EXIT");

        // ������ǿ�ƽ���
        System.exit(0);

        // ����ִ�е�����
        System.out.println("main:END");
    }
}
