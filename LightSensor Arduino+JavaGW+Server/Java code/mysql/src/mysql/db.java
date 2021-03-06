package mysql;

import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

import com.mysql.jdbc.Connection;
import com.mysql.jdbc.Statement;


 
public class db {
	//設定server IP,帳號,密碼
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";//設定JDBC driver  
	static final String DB_URL = "jdbc:mysql://192.168.1.111/iot";//server IP後街資料庫名稱
	static final String USER = "iot";
	static final String PASS = "iot";
    public static void main(String[] argv) {
    	
    	//call to ensure the driver is registered
        try
        {
            Class.forName(JDBC_DRIVER);
        } 
        catch (ClassNotFoundException e) {
            System.out.println("MySQL JDBC Driver not found !!");
            return;
        }

        Connection connection = null;//建立Connection物件
        Statement statement = null;//建立Statement物件
        try {
        	//連接mysql database
            connection = (Connection) DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("SQL Connection to database established!");
            
            //執行query
            statement = (Statement) connection.createStatement();//建立一個物件傳送SQL statement到database
            String sql= "SELECT * FROM light";
            ResultSet rs = statement.executeQuery(sql);//執行sql語法，回傳語法結果
 
          
            while(rs.next()){
                //檢索每行的欄位
                int id  = rs.getInt("id");
                int value = rs.getInt("value");
 
                //將value print出來
                System.out.print("Id: " + id);
                System.out.println(", Value: " + value);

             }
            rs.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
        	//Handle errors for JDBC
            System.out.println("Connection Failed! Check output console");
            return;
        } finally {
            try
            {
                if(connection != null)
                    connection.close();
                System.out.println("Connection closed !!");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
