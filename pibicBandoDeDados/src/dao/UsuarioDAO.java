/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dao;

import dto.Usuario;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;
/**
 *
 * @author heloh
 */
public class UsuarioDAO {
     Connection conn;

    public ResultSet autenticacaoUsuario(Usuario objUsuario) {

        conn = new ConexaoDAO().conexaoBD();

        try {

            String sql = "select * from usuario where nome_usuario = ? and senha_usuario = ? ";
            PreparedStatement pstm = conn.prepareStatement(sql);

            pstm.setString(1, objUsuario.getUsuario());
            pstm.setString(2, objUsuario.getSenha());

            ResultSet rs = pstm.executeQuery();
            return rs;

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "UsuarioDAO: " + e);
            return null;
        }
    }
}
