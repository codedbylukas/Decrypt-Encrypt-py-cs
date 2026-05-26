using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace SecureFileEncryptionNamespace
{
    public static class SecureFileEncryption
    {
        public static void EncryptFileInPlace(string path, string password, string saltString)
        {
            try
            {
                byte[] salt = Encoding.UTF8.GetBytes(saltString);
                byte[] originalData = File.ReadAllBytes(path);
                byte[] encryptedData;

                // Modernes 'using' verhindert tiefe Einrückungen
                using var keyDerivation = new Rfc2898DeriveBytes(password, salt, 10000, HashAlgorithmName.SHA256);
                byte[] key = keyDerivation.GetBytes(32); // 256 Bit
                byte[] iv = keyDerivation.GetBytes(16);  // 128 Bit

                using (var aes = Aes.Create())
                {
                    aes.Key = key;
                    aes.IV = iv;

                    using (var ms = new MemoryStream())
                    {
                        using (var cs = new CryptoStream(ms, aes.CreateEncryptor(), CryptoStreamMode.Write))
                        {
                            cs.Write(originalData, 0, originalData.Length);
                        }
                        encryptedData = ms.ToArray();
                    }
                }

                File.WriteAllBytes(path, encryptedData);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error occurred while encrypting file: {ex.Message}");
                throw;
            }
        }
    }
}