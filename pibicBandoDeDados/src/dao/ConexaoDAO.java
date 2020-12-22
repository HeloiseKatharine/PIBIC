package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.TimeZone;
import javax.swing.JOptionPane;

/**
 *
 * @author heloh
 */
public class ConexaoDAO {
    public Connection conexaoBD(){
        
        Connection conn = null;
        
        try {
        
            String url = "jdbc:mysql://localhost:3306/mamografia?user=root&password=root" ;
            /*?useTimezone=true&serverTimezone=UTC*/
            /*Drive de conexão | local da base de dados | nome do banco | usuario | senha*/
            conn = DriverManager.getConnection(url);
        
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "ConexaoDAO " + e.getMessage());        
        }    
        return conn;
    }
}
