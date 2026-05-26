using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace SecureFileDecryptionNamespace
{
    public static class SecureFileDecryption
    {
        public static void DecryptFileInPlace(string path, string password, string saltString)
        {
            try
            {
                byte[] salt = Encoding.UTF8.GetBytes(saltString);
                
                using (Rfc2898DeriveBytes keyDerivation = new Rfc2898DeriveBytes(password, salt, 10000, HashAlgorithmName.SHA256))
                {
                    byte[] key = keyDerivation.GetBytes(32); // 256 Bits
                    byte[] iv = keyDerivation.GetBytes(16);  // 128 Bits
                    byte[] originalData = File.ReadAllBytes(path);
                    byte[] decryptedData;

                    using (Aes aes = Aes.Create())
                    {
                        aes.Key = key;
                        aes.IV = iv;

                        using (MemoryStream ms = new MemoryStream())
                        {
                            using (CryptoStream cs = new CryptoStream(ms, aes.CreateDecryptor(), CryptoStreamMode.Write))
                            {
                                cs.Write(originalData, 0, originalData.Length);
                            }
                            decryptedData = ms.ToArray();
                        }
                    }

                    File.WriteAllBytes(path, decryptedData);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error occurred while decrypting file: {ex.Message}");
                throw;
            }
        }
    }
}
