import java.net.HttpURLConnection;
import java.net.URL;

import java.io.OutputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;

import java.util.Scanner;

public class fact_client {
   public static void main(String[] args) throws Exception{
      String Url ="http://127.0.0.1:5000/facty";

      System.out.print("Enter a number: ");
      Scanner sc = new Scanner(System.in);
      int num = sc.nextInt();
      String JSON_playload = "{\"num\":"+num+"}";
      sc.close();

      URL obj = new URL(Url);
      HttpURLConnection con = (HttpURLConnection)obj.openConnection();
      con.setRequestMethod("POST");
      con.setRequestProperty("Content-Type", "application/json");
      con.setDoOutput(true);

      OutputStream ops = con.getOutputStream();
      ops.write(JSON_playload.getBytes());
      ops.flush();
      ops.close();

      BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
      String inline;
      StringBuffer response =new StringBuffer();
      int resCode = con.getResponseCode();

      while ((inline = br.readLine()) != null) {
         response.append(inline);
      }
      br.close();

      System.out.println("Response code: "+resCode);
      System.out.println("Response: "+response.toString());
   }
}
