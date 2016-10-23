import java.util.*;

public class FoodTruck {
	public static final void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNextLine()) {
			System.out.println(in.nextLine());
		}
	}

	public static double haversine(double lat1, double long1,
                                   double lat2, double long2) {
		lat1 = deg_to_rad(lat1);
		long1 = deg_to_rad(long1);
		lat2 = deg_to_rad(lat2);
		long2 = deg_to_rad(long2);
	}

	public static double deg_to_rad(double degrees) {

	}
}
