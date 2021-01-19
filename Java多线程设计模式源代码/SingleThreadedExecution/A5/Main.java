public class Main {
    public static void main(String[] args) {
        System.out.println("Testing SecurityGate...");
        SecurityGate gate = new SecurityGate();
        CrackerThread[] t = new CrackerThread[100];

        // CrackerThread����
        for (int i = 0; i < t.length; i++) {
            t[i] = new CrackerThread(gate);
            t[i].start();
        }

        // CrackerThread������
        for (int i = 0; i < t.length; i++) {
            try {
                t[i].join();
            } catch (InterruptedException e) {
            }
        }

        // ȷ��
        if (gate.getCounter() == 0) {
            System.out.println("SecurityGate may be safe.");
        } else {
            System.out.println("SecurityGate is NOT safe!");
            System.out.println("getCounter() == " + gate.getCounter());
        }
    }
}
