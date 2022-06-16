from os import listdir, mkdir, path
from shutil import move


# TODO: Try with regex instead of list of ext


class FileOrganizer:
    """Organize files of given location or downloads directory."""

    LOCATION = "C://Users//Sahil//Downloads"

    IMAGE_EXT = [".jpg", ".png", ".jpeg", ".gif", ".webp", ".eps"]
    DOC_EXT = [
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".pdf",
        ".txt",
        ".odt",
        ".ods",
        ".epub",
        ".pages",
        ".pub",
        ".word",
        ".md",
        ".mdx",
        ".dot",
        ".dotx",
    ]
    VIDEO_EXT = [
        ".mp4",
        ".mov",
        ".avi",
        ".wmv",
        ".avchd",
        ".flv",
        ".f4v",
        ".swf",
        ".mkv",
        ".webm",
        ".mpeg-2",
    ]
    MUSIC_EXT = [
        ".mp3",
        ".aac",
        ".flac",
        ".alac",
        ".wav",
        ".aiff",
        ".dsd",
        ".pcm",
        ".ogg",
        ".wma",
    ]
    ZIP_EXT = [
        ".7z",
        ".gzip",
        ".zip",
        ".xz",
        ".bzip2",
        ".rar",
        ".rar5",
        ".tar",
        ".cab",
        ".lha",
        ".tgz",
    ]

    def __init__(self, location=None):
        self.location = location if location else FileOrganizer.LOCATION
        self.image_location = ""
        self.doc_location = ""
        self.video_location = ""
        self.music_location = ""
        self.zip_location = ""
        self.other_location = ""
        complete_list = listdir(self.location)
        self.file_list, self.dir_list = self.make_file_list(complete_list)

    def make_file_list(self, complete_list: list) -> tuple[list, list]:
        """Return list of files and directory based on passed list."""
        file_list = []
        dir_list = []
        for file in complete_list:
            file_path = path.join(self.location, file)
            if path.isfile(file_path):
                file_list.append(file_path)
            else:
                dir_list.append(file_path)
        return file_list, dir_list

    def check_directory(self, dir_location: str) -> None:
        """Check if directory exists or not. If not create one."""
        if not path.exists(dir_location):
            mkdir(dir_location)

    def file_mover(self, extention_list, new_location):
        """move file based on extension list to new location."""
        for file in self.file_list:
            if (path.splitext(file)[1]).lower() in extention_list:
                move(file, new_location)

    def organize_images(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        self.image_location = path.join(self.location, "Organized Images")
        self.check_directory(self.image_location)

        self.file_mover(FileOrganizer.IMAGE_EXT, self.image_location)

    def organize_docs(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        self.doc_location = path.join(self.location, "Organized Documents")
        self.check_directory(self.doc_location)

        self.file_mover(FileOrganizer.DOC_EXT, self.doc_location)

    def organize_videos(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        self.video_location = path.join(self.location, "Organized Videos")
        self.check_directory(self.video_location)

        self.file_mover(FileOrganizer.VIDEO_EXT, self.video_location)

    def organize_music(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        self.music_location = path.join(self.location, "Organized Musics")
        self.check_directory(self.music_location)

        self.file_mover(FileOrganizer.MUSIC_EXT, self.music_location)

    def organize_zip(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""
        self.zip_location = path.join(self.location, "Organized Zip Files")
        self.check_directory(self.zip_location)

        self.file_mover(FileOrganizer.ZIP_EXT, self.zip_location)

    # def organize_others(self):
    #     """Organize images based on jpg, jpeg, png, gif, webp extensions."""
    #     self.other_location = path.join(self.location, "Organized Other Files")
    #     self.check_directory(self.other_location)

    #     self.file_mover(FileOrganizer.IMAGE_EXT, self.image_location)

    def call_all(self):
        """Call all mover methods"""
        self.organize_images()
        self.organize_docs()
        self.organize_music()
        self.organize_videos()
        self.organize_zip()


FileOrganizer().call_all()

# get Extension
# ext = splitext("/Downloads/Frame 5.png")[1]
# print(ext)
