
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class client {

   public static void main(String[] args) throws Exception {
      String url = "http://localhost:5000/convert";
      Scanner scanner = new Scanner(System.in);

      double amountInRs = getUserInput(scanner);

      String jsonInputString = createJsonPayload(amountInRs);

      HttpURLConnection connection = setupConnection(url);
      sendRequest(connection, jsonInputString);

      handleResponse(connection);

      scanner.close();
      connection.disconnect();
   }

   private static double getUserInput(Scanner scanner) {
      System.out.print("Enter the amount you want to convert: ");
      return scanner.nextDouble();
   }

   private static String createJsonPayload(double amountInRs) {
      return "{\"amount_in_rs\": " + amountInRs + "}";
   }


   private static HttpURLConnection setupConnection(String url) throws Exception {
      final URL obj = new URL(url);
      HttpURLConnection connection = (HttpURLConnection) obj.openConnection();
      connection.setRequestMethod("POST");
      connection.setRequestProperty("Content-Type", "application/json");
      connection.setDoOutput(true);
      return connection;
   }

   private static void sendRequest(HttpURLConnection connection, String jsonInputString) throws Exception {
      try (OutputStream os = connection.getOutputStream()) {
         os.write(jsonInputString.getBytes());
         os.flush();
      }
   }

   private static void handleResponse(HttpURLConnection connection) throws Exception {
      int responseCode = connection.getResponseCode();
      BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
      String inputLine;
      StringBuffer response = new StringBuffer();

      while ((inputLine = in.readLine()) != null) {
         response.append(inputLine);
      }
      in.close();

      System.out.println("Response Code: " + responseCode);
      System.out.println("Response: " + response.toString());}
}