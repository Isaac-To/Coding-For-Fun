import java.util.Arrays;
import java.util.Scanner;

class appleDivision extends Thread {
    private static int min = Integer.MAX_VALUE;

    private static int[] args;

    private static int length;

    private static void changeMin(int a) {
        min = a;
        System.out.println(min);
    }

    private static void swap(int i, int j) {
        int temp = args[i];
        args[i] = args[j];
        args[j] = temp;
    }

    private static void minimumLeeWay() {
        //returns the smallest division of the array
        for (int i = 0; i < length / 2 + 1; i++) {
            int sum = Math.abs(Arrays.stream(Arrays.copyOfRange(args, 0, i)).sum() - Arrays.stream(Arrays.copyOfRange(args, i, length)).sum());
            if (sum < min) {
                changeMin(sum);
            }
        }
    }

    private static void permutate(int size) {
        if (size == 1) {
            minimumLeeWay();
            return;
        }  
        for (int i = 0; i < size; i++) {
            permutate(size - 1);
            if (size % 2 == 1) {
                swap(0, size - 1);
            }
            else {
                swap(i, size - 1);
            }
        }
    }

    public static void main(String[] noArgs) {
        //input taker
        Scanner sc = new Scanner(System.in);
        args = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        sc.close();
        length = args.length;
        permutate(length);
        System.out.println(min);
    }
}