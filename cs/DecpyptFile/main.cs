using System;
using System.Data.SqlTypes;
using System.IO;
using System.Security.Cryptography;
using System.Text;

class SecureFileEncryption
{
    public static void EncryptFileInPlace(string path, string password, string SaltString)
    {
        byte[] salt = Encoding.UTF8.GetBytes("festerSaltWert");

        using (Rfc2898DeriveBytes keyDerivation = new(password, salt, 10000, HashAlgorithmName.SHA256))
        {
            byte[] key = keyDerivation.GetBytes(32); // 256 Bit
            byte[] iv = keyDerivation.GetBytes(16);  // 128 Bit

            byte[] originalData = File.ReadAllBytes(path);
            byte[] encryptedData;

            using (Aes aes = Aes.Create())
            {
                aes.Key = key;
                aes.IV = iv;

                using (MemoryStream ms = new MemoryStream())
                {
                    using (CryptoStream cs = new CryptoStream(ms, aes.CreateEncryptor(), CryptoStreamMode.Write))
                    {
                        cs.Write(originalData, 0, originalData.Length);
                    }
                    encryptedData = ms.ToArray();
                }
            }

            File.WriteAllBytes(path, encryptedData);
        }
    }
}