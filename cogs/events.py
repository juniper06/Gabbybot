from asyncio import events
import discord
import random 
from discord.ext import commands

pictures = [
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/274363011_2140244822820964_3108051005386696065_n.png?_nc_cat=109&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeGjBvlawKikb1JxtKIfmUnhaqb7XnB23nFqpvtecHbecfXkacCK4F29qSB5JiPuhGyVQsinTZPAmYkU7JNWT1yP&_nc_ohc=W-0i5C0rVBsAX-n0d8n&tn=RgY4HBKM29zNIyrU&_nc_ht=scontent.fceb6-1.fna&oh=03_AVKEMO0a881eyLWPLIsL-wGmsw95CpbxXRmuEb-mP4OsEA&oe=627D3C00",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/277311991_393159802736347_2589135513708898153_n.png?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeFS7u2uq3fY2y5lnUvyE_JxfE8RNT82C918TxE1PzYL3c043XGAmUtJLoWyYARVgD7VLTSh9wcqhDFPAF4bTdRJ&_nc_ohc=AVUrYWzH5KgAX80EwYk&tn=RgY4HBKM29zNIyrU&_nc_ht=scontent.fceb6-1.fna&oh=03_AVLlE4F_S9cwqWlJO4YklQpxFeNZa3Jo-T6ucnp0cK5rUQ&oe=627C7321",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/277140881_309662157941454_6077383992412010057_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeGI62iXF4Qwc_pJYZefBZ9VlfxvULzKKqWV_G9QvMoqpQ1Ry8NauSSYkjnO2tf-xMy8Z57IQjWSwQs_znpln0wN&_nc_ohc=y3VK6l3708EAX-gtpg5&_nc_ht=scontent.fceb6-1.fna&oh=03_AVJ-uDTKreISC5_-Bh-OvDCuiluSumNS0Ac3TkvsOiVw2g&oe=627BC025",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/275928407_713200270013892_6295780581232214128_n.png?_nc_cat=108&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeHpyuntwQYbCX9SaGjzDVElUTO-to3hbJ1RM762jeFsnaYuhA3KcsTw8-cdzuLGRBCF9l0rxtET_Pa-lijo5DHz&_nc_ohc=HlO-iscdgfQAX-TowIF&_nc_oc=AQkkSXhyxjWt8nCxWwiBM_MgT3muRgHgbgCyaB_YdCQ4pkS6-XcVMGBbVam_p28_Pu4&_nc_ht=scontent.fceb6-1.fna&oh=03_AVJLWZR-80qy1m-WqIASUdMSrQLKOLx_erwE0kfkln3Zsw&oe=627E5A35",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/277179054_496653118764421_959658918781689222_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeGyLqvtskZZdGbUixKAD_eMxa84jYCffW7FrziNgJ99bjLPIow7F0_O6X3iNIJIwE3q3DSPNcHJphbpqe1tLqCA&_nc_ohc=nACr17nW9iIAX8zzKSJ&_nc_ht=scontent.fceb6-1.fna&oh=03_AVKw2iLrSb3D_vImkoTy8LkwdlwGjjljffKiPl84jgu9sg&oe=627B85C1",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/276977382_1269825597280324_6804815538502634427_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeETf1R464TAr4aNtimlolU5YlPdJ7QmIhtiU90ntCYiG5MHm081nUnRdlk_Q5NG5yK9THNc6K2M-c71UsZsXByF&_nc_ohc=oRdf_HISgWQAX9N7B5-&tn=RgY4HBKM29zNIyrU&_nc_ht=scontent.fceb6-1.fna&oh=03_AVKYKhq0bbCutolPqXXRZbUreQW_G4orLT6bIz6Ci9jD6A&oe=627D3590",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/275395976_510269997438126_968813543945062655_n.png?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeG8ba-U-kqhxOJn_RD9TSZvoW8QaZlBg0GhbxBpmUGDQXYZ9x8mqKeH80kGmYJgQBdd5GDetUR0jd9IyoZg082q&_nc_ohc=hbz0jdJvxbIAX-O6q41&_nc_ht=scontent.fceb6-1.fna&oh=03_AVII7w3fjOpx6KYvhdlptqM13pgDoK39Mz2Vpom5qukz6Q&oe=627C2E29",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/275595728_1149286322488361_2466135002186633965_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeGTxWt3QvDpJ2q7uvxWUOL02DxEYDC4PsfYPERgMLg-x5kS0pV63tGdvxEbwgdWchlFvwcLJ6wEDaYvwKftQxfL&_nc_ohc=YeYiIeNUq_UAX-QCypS&_nc_ht=scontent.fceb6-1.fna&oh=03_AVJ7ZPRujNk4tkN2L4pJ9gBW_KJBp8DW0unnx_23lluAKA&oe=627C4C55",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/277176985_374020354604277_6887505743110250405_n.png?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeF4UqZ_Azj5NOIGQI0GM0RHcNQUZ4BIkJ1w1BRngEiQnaalcpqqRCBcIWx102j64GeGHepAPRNUA4zeVPY0dDR2&_nc_ohc=M4yiG836VdoAX_8Im8m&_nc_oc=AQkpPHeRnVLJ2E4pIBy8ssHf9XFa8YugnBEe1IomkULHyANJXYNOWNCaXfv6spySM50&_nc_ht=scontent.fceb6-1.fna&oh=03_AVIOSTdhbgGEVuRaHmOIQLTeT-at-nOfL1Qxz4hL02925w&oe=627B6DFD",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/273801395_324850259586758_7831105790271173936_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeHk0zpbNhCN2x4jg_oMTNDN0T1ty-Ml2BHRPW3L4yXYEdN7bqtepeK7DP2ZlJLDu1RJdCXCV-ARxtguT78YQuI9&_nc_ohc=MqPUELQY1w0AX-If4g1&_nc_ht=scontent.fceb6-1.fna&oh=03_AVLPtlDz_gtxEo4NF0L6vLtQ8ZvGZryq4vuWWJS8rRv5vw&oe=627EC4AE",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/275186950_1004925296786288_1223152785529862704_n.png?_nc_cat=106&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeF99EJsiH7erSnks9hQKyfhK2547LXfQfcrbnjstd9B91PDBunMeN2zQP4ZS8zNs2fDtp5EoHu4C5zmlpm0QzHx&_nc_ohc=7m5AGLd4SBEAX9kvxu6&tn=RgY4HBKM29zNIyrU&_nc_ht=scontent.fceb6-1.fna&oh=03_AVKLgzs4EXZdWaoo7PIau946LWojlX6f6_ARYmX9iCSVlA&oe=627C723F",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/274782612_706280670530649_3209049740193318596_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeHJ57Z8V99LP9G-6q8tnM7vvR3Ix2wXIi69HcjHbBciLmBQ77qJH2MW4aWJ877bI65XBIoBA29mxvh5XW_45HCx&_nc_ohc=geCVSgvMezoAX9jiuAI&_nc_ht=scontent.fceb6-1.fna&oh=03_AVJ-8VOvAoFH6ld3Ifds8K1zWnkh3bwyCvtIIL_WviuSGA&oe=627E15B4",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/275432989_329147105852878_6888376932782481220_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeGKF9g7XZWpryo0NW_glN2wrAqCaCm2WlSsCoJoKbZaVAmFzF2C2h7QiCqx9jrmVRRR34TKi2nANSOJ5MC6WEfW&_nc_ohc=xdYexRyE3iYAX--amE4&_nc_oc=AQk2llWm4ohUxx2sCU8G6wIqtNrcO-ZKq7o534ezbUqm2n09C2x1NNJL0ZfjXVclATM&_nc_ht=scontent.fceb6-1.fna&oh=03_AVKpkDkwwuIECSEKwYvQgL5drcQdLr7wUpZbiCsV7_4X6Q&oe=627E2850",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/275435846_484529533118694_4605724160558902861_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeHAOAGUMwpje5WdzmO6mbl-c_hbFbvHV3Jz-FsVu8dXcrQyNyj6wHvWKdaKW4nrBPyttteDpPtbWinRSquqwcpk&_nc_ohc=-bzcaS0R8P4AX_Qg5De&_nc_ht=scontent.fceb6-1.fna&oh=03_AVIcsiM4MH2iyHjCiwcnBOkDeUvRZZp9vS8i9LvxFdeINg&oe=627F1E90",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/274584944_805424970416024_5755044203323558561_n.png?_nc_cat=105&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeFdHLg09kcSp8xQDvf80vopzCC2HPFVJILMILYc8VUkgjvOt-c5dNykzIMP0S7oeTOvaY939CTY75bP5Z0ritiK&_nc_ohc=la_pSSGzcAIAX9FL5tb&_nc_ht=scontent.fceb6-1.fna&oh=03_AVJ8LQhH-Eb5nk0WGZ4ZWTmyHxiFz_hMWseFb3fmHFA2vw&oe=627D95BE",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/274725913_387504836061951_9067570818219190508_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeH-AXAdlpS0h5Flrm2COwYOx3UJu07-z3zHdQm7Tv7PfBj0dEYApAZpl4EQRWwlFyEci1QV24Lb_JtkCBiS3GZu&_nc_ohc=IYqmY_slevsAX_Ht3u_&tn=RgY4HBKM29zNIyrU&_nc_ht=scontent.fceb6-1.fna&oh=03_AVIr0Q63ZyfdYhs7cet4P9WaQCimb3GX73w-nua5eTFpHg&oe=627D4D63",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/274380247_650042059444943_2784511659800245226_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeGD3asFpcnnpRco7Yut-Z0gVnhgLJ-1MTVWeGAsn7UxNVlfq_gBIk3c2IUL2-TCE_mshY9xCusBk7zbJDVYnfKK&_nc_ohc=_WzmpPrwWk8AX982_2d&_nc_ht=scontent.fceb6-1.fna&oh=03_AVKWmWJz_3Ym_cSUDBvG4R1McUoLlDFnlGs8DTjGMUuiFg&oe=627D59DE",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/275047521_366527611777785_9118613867807709268_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeG4BwnP-wlkpIE_i56dYEOxrTYFdin5MGGtNgV2KfkwYbXbr-yzai1M0PNYofva26wySUUOdI4jTnFziL8xsDhZ&_nc_ohc=b_fYlI2WyZgAX-Z7v4B&tn=RgY4HBKM29zNIyrU&_nc_ht=scontent.fceb6-1.fna&oh=03_AVJBas-DovsiMT5aaN6tDivyuPM7cSVhTdI5nVaQu-CDaA&oe=627BF9C2",
    "https://scontent.fceb6-1.fna.fbcdn.net/v/t1.15752-9/274488675_665126011578715_5777758757841277956_n.png?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeEcDsjzThY1WwhKzu3OpDIXowJEYJf7az-jAkRgl_trPxYUlif4mYon9hlr7biiR6fHpIZugs-yCWUVxwrY_zJ2&_nc_ohc=ub_8sjjfH_gAX8n60pI&_nc_ht=scontent.fceb6-1.fna&oh=03_AVLn65D39gD-AgV3277H0JwjYKjS0MXYshkCRx9QdhBH7A&oe=627B7759",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/274716445_1346028459203814_1223274692289370771_n.png?stp=dst-png_s261x260&_nc_cat=104&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeFK0O25UVyJAQXt6WoAqKS1CEZcmAP2llkIRlyYA_aWWcCV-CeCCj_Hs2XUNpLjZTPw-o-07ThEgNyuJoaUvRq2&_nc_ohc=OGlnSxmp81AAX_-UD_D&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVJSZrti_1NwQIcAtr14SNX88RpJ9tp77HvfYGnf9PQyKQ&oe=62599C43",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/274806047_383002423241275_6003369017191784106_n.jpg?stp=dst-jpg_s320x320&_nc_cat=106&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeFOLbXhYTaaF5whplXTp0zsZmHwUstZOvhmYfBSy1k6-MvJbKOLsjRZxOhj4yCABMmEu17kcZus3YPkDf-uDCmh&_nc_ohc=ypcMslwoeM0AX_0DHy-&_nc_oc=AQn7pynwrJTHUD70T1DWcD9LiCQnzJdFKmGkWvBlavLwuv3RLdoNM6Lh6UCISgzXnonL6ehuEHCjuMqS5rbqLTXx&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVKhz5h6MDP9M-GE0w5Mj-qPWT1kLlp1UCWj8C5oAfgMdA&oe=627DDCBC",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/275094563_208499181472534_3707053431891146565_n.jpg?stp=dst-jpg_s526x296&_nc_cat=106&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeGg8slQ4RCStKxK1P65VdPEW9gW2O5fqmtb2BbY7l-qayQ8Qt2DxAhQTIdNP9G27jelkojAxReCPwm0Ahw449a1&_nc_ohc=A3r_SIpBtvwAX9OIiIM&_nc_oc=AQkjIZZkNKuBSDUD4S5DOyU0oh0uKVsJ3H_oDGESAdJP2AvIjm_YxdVi4lffced6g_t_jr68uUBUIjc-OTDowf-V&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVKvznRnG-4Nh91Zc4CXLYc8j7o79IiH3CB2AtykOcDx1Q&oe=627F0A37",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/275179911_1140837330064247_3084918620312299261_n.jpg?stp=dst-jpg_s350x350&_nc_cat=105&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeHv3MTTCnjN-yoCN4c7rFGkW1Ym5L1rmDdbVibkvWuYN6gxqvzCnf5-ZW-0QAd1GhjStPD_mEgLQnve9QNgpoc8&_nc_ohc=2XcvMuGIe5EAX9C1F_n&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVL1MPPXFf0T48srPdFlEjMjdmyb9zh9FeTKuCw_t9v4JQ&oe=627C6D28",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/274619320_5642047102495863_6722646736388214895_n.jpg?stp=dst-jpg_s851x315&_nc_cat=103&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeFjT3Ul-iFZdPjCKmo8zwqidrq41yauO4x2urjXJq47jDnDv9ImbqbJzvwoHEBtbo_a2P-EOf6Mo4fCnWozq6nZ&_nc_ohc=hinmOunpjAUAX9wbmn6&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVJnljiuGW4stFJVusiDBIufTYuVUzvuiw5O7RRhnkD5rg&oe=627C5292",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/274608567_1027558291306718_5603830228202341328_n.jpg?stp=dst-jpg_s851x315&_nc_cat=103&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeGryYuGp-vOZmslyWNWHCLLu7b1i-OakAO7tvWL45qQA_0U6JVYluBJ5xYP72q5K8TQQ5wXyOxpQKxJ6dJgWYp_&_nc_ohc=bLeMs_xYknsAX94NlkK&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVLIbzEg5L3k1wEPf3jr3LorA9zd2mtKObfx0heJhQ0n5A&oe=627CE9B0",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/274976867_956756524859443_1415015026014584107_n.jpg?stp=dst-jpg_s206x206&_nc_cat=105&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeEJVI4AgRGSGgnkXJq-3AkBW-psQgVc1Ptb6mxCBVzU-yCmFmvVrEqVe2btV41mVfGntUE3uACEzq6CzFyhzZOg&_nc_ohc=TQwSdG0yWuIAX8pGxWr&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVL6eq57lV1aeMcghhMu8ee34ZKB9IpNAKuYiSwwUg3DJg&oe=6258C880",
    "https://scontent.xx.fbcdn.net/v/t1.15752-9/274959204_996335167659538_480372284298685699_n.jpg?stp=dst-jpg_p206x206&_nc_cat=105&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeH0an6RWBPxWk-AD6BuZpZAE8Y-ixSS97MTxj6LFJL3s1xE1c9kBo2RU_s1Tc5pFHVq7ScFQvLlZJUG-guCHNyN&_nc_ohc=H3RmPtq5mvAAX_u-0AZ&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVLWP5Aoqe8AdEF-ZmeLEK_TTjEEZg0HwCZD5e2FyxHa-g&oe=6258F57A"
]

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client.user} the bot has been activated!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title=f"Hi! {member.name}")
            embed.add_field(name="Welcome to the Kulto de Morax ",
                            value='Putang ina mo')
            embed.set_image(url=random.choice(pictures))
            embed.set_author(name = member.name,url=member.avatar_url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client:
            return
        if message.content.startswith("#include"):
            await message.delete()
            embed = discord.Embed(title="C or CPP code")
            codes = '''```cpp\n{}\n```'''.format(message.content)
            embed.description = codes
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
            

def setup(client):
    client.add_cog(Events(client))