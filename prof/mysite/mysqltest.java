import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;
public class mysqltest{
    private final String USER_AGENT = "Mozilla/5.0";
    public static void main(String[] args) throws Exception{
        mysqltest http = new mysqltest();

	System.out.println("Testing Send Http POST request");
	http.sendPost();

    }

    private void sendPost() throws Exception{
	String url = "http://localhost:8001/mysql.php";
	URL obj = new URL(url);
	HttpURLConnection con = (HttpURLConnection) obj.openConnection();

	//add request header
	con.setRequestMethod("POST");
	con.setRequestProperty("User-Agent", USER_AGENT);
	con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
	
	String urlParameters = "func=2&class=CS%20475&prof=admin&startdate=2017-02-12&enddate=2017-02-14&student=800069528";

	//Send post request
	con.setDoOutput(true);
	DataOutputStream wr = new DataOutputStream(con.getOutputStream());
	wr.writeBytes(urlParameters);
	wr.flush();
	wr.close();

	int responseCode = con.getResponseCode();
	System.out.println("\nSending 'POST' request to URL: " + url);
	System.out.println("Post parameters: " + urlParameters);
	System.out.println("Response code: " + responseCode);

	BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
	String inputLine;
	StringBuffer response = new StringBuffer();

	while ((inputLine = in.readLine()) != null){
	    response.append(inputLine);
	}
	in.close();

	//print result
	System.out.println(response.toString());

    }

}
