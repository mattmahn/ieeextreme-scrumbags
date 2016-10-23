import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.stream.Collectors;

public class FoodTruck {
    private static final double EARTH_RADIUS = 6378.137; /* kilometers */
    private static SimpleDateFormat dateFormat =
            new SimpleDateFormat("MM/dd/yyyy HH:mm");
    private static Map<String, Date> phones = new TreeMap<>();
    private static LinkedList<Person> people = new LinkedList<>();

    public static void main(String[] args) throws ParseException {
        Scanner in = new Scanner(System.in);

        String[] madhuPos = in.nextLine().trim().split(",");
        double madhuLat = Double.parseDouble(madhuPos[0]);
        double madhuLong = Double.parseDouble(madhuPos[1]);

        double searchRadius = Double.parseDouble(in.nextLine().trim());

        in.nextLine(); /* don't care about CSV header */

        while (in.hasNextLine()) {
            String[] vals = in.nextLine().trim().split(",");
            Date date = dateFormat.parse(vals[0]);
            double lat = Double.parseDouble(vals[1]),
                    lon = Double.parseDouble(vals[2]);
            String phoneNum = vals[3];
            Person person = new Person(lat, lon, phoneNum, date);
            phones.put(phoneNum, date);
            if (phones.get(phoneNum).getTime() > date.getTime()) {
                person.date = phones.get(phoneNum);
            }
            people.add(person);
        }

        LinkedList<String> closePeople =
                people.stream()
                      .filter(person -> isClose(person.lat, person.lon,
                                                madhuLat, madhuLong,
                                                searchRadius))
                      .sorted()
                      .map(p -> p.phone)
                      .distinct()
                      .collect(Collectors.toCollection(LinkedList<String>::new));
        System.out.println(String.join(",", closePeople));
    }

    public static boolean isClose(double lat1, double long1,
                                  double lat2, double long2,
                                  double radius) {
        return haversine(lat1, long1, lat2, long2) <= radius;
    }

    public static double haversine(double lat1, double long1,
                                   double lat2, double long2) {
        lat1 = deg_to_rad(lat1);
        long1 = deg_to_rad(long1);
        lat2 = deg_to_rad(lat2);
        long2 = deg_to_rad(long2);

        return 2 * EARTH_RADIUS * Math.asin(
                Math.sqrt(
                        Math.pow(Math.sin((lat1 - lat2) / 2), 2) +
                        Math.cos(lat1) *
                        Math.cos(lat2) *
                        Math.pow(Math.sin((long1 - long2) / 2), 2)
                )
        );
    }

    public static double deg_to_rad(double degrees) {
        return degrees * Math.PI / 180;
    }

    static class Person implements CharSequence, Comparable<Person> {
        double lat, lon;
        String phone;
        Date date;

        public Person(double lat, double lon, String phone, Date date) {
            this.lat = lat;
            this.lon = lon;
            this.phone = phone;
            this.date = date;
        }

        @Override
        public boolean equals(Object o) {
            if (o instanceof Person) {
                Person p = (Person) o;
                return p.phone.equals(this.phone);
            }
            return false;
        }

        @Override
        public String toString() {
            return phone;
        }

        @Override
        public int length() {
            return phone.length();
        }

        @Override
        public char charAt(int i) {
            return phone.charAt(i);
        }

        @Override
        public CharSequence subSequence(int i, int i1) {
            return phone.subSequence(i, i1);
        }

        @Override
        public int compareTo(Person person) {
            return phone.compareTo(person.phone);
        }
    }
}
