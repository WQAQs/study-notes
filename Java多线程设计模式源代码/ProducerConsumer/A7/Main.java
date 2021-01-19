public class Main {
    public static void main(String[] args) {
        // ִ��Host�Ĵ��ʹ�����߳�
        Thread executor = new Thread() {
            public void run() {
                System.out.println("Host.execute BEGIN");
                try {
                    Host.execute(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Host.execute END");
            }
        };

        // ����
        executor.start();

        // ��ϢԼ15��
        try {
            Thread.sleep(15000);
        } catch (InterruptedException e) {
        }

        // ִ��ȡ������
        System.out.println("***** interrupt *****");
        executor.interrupt();
    }
}
