<template>
  <div class="p-6 bg-gray-50 min-h-screen">
    <div
      class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6 gap-4"
    >
      <h1 class="text-2xl font-bold text-blue-800">📚 Book List</h1>
      <button
        class="px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
        @click="openAddModal"
      >
        ➕ Add Book
      </button>
    </div>

    <div class="overflow-x-auto shadow-md rounded-lg bg-white">
      <table class="min-w-full table-auto border-collapse">
        <thead class="bg-gradient-to-r from-blue-500 to-blue-700 text-white">
          <tr>
            <th class="py-3 px-6 text-center font-semibold text-sm">Title</th>
            <th class="py-3 px-6 text-center font-semibold text-sm">Author</th>
            <th class="py-3 px-6 text-center font-semibold text-sm">ISBN</th>
            <th class="py-3 px-6 text-center font-semibold text-sm">
              Available Copies
            </th>
            <th class="py-3 px-6 text-center font-semibold text-sm">Actions</th>
          </tr>
        </thead>
        <tbody class="text-gray-700">
          <tr
            v-for="book in books"
            :key="book.id"
            class="even:bg-gray-50 hover:bg-blue-100 transition duration-200"
          >
            <td class="py-3 px-6 text-center">{{ book.title }}</td>
            <td class="py-3 px-6 text-center">{{ book.author }}</td>
            <td class="py-3 px-6 text-center">{{ book.isbn }}</td>
            <td class="py-3 px-6 text-center">{{ book.available_copies }}</td>
            <td class="py-3 px-6 text-center space-x-2">
              <button
                class="bg-yellow-500 text-white px-4 py-2 rounded-md hover:bg-yellow-600 transition"
                @click="openEditModal(book)"
              >
                ✏️ Edit
              </button>
              <button
                class="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600 transition"
                @click="openDeleteModal(book)"
              >
                🗑️ Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add/Edit Modal -->
    <BookFormModal
      :visible="isModalOpen"
      :book="selectedBook"
      @close="isModalOpen = false"
      @saved="handleSaved"
    />

    <!-- Confirm Delete Modal -->
    <ConfirmDeleteModal
      :visible="isConfirmVisible"
      :itemName="bookToDelete?.title"
      @close="isConfirmVisible = false"
      @confirm="deleteBook"
    />
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "vue3-toastify";
import BookFormModal from "@/components/BookFormModal.vue";
import ConfirmDeleteModal from "@/components/ConfirmDeleteModal.vue";

export default {
  name: "BookList",
  components: {
    BookFormModal,
    ConfirmDeleteModal,
  },
  data() {
    return {
      books: [],
      isModalOpen: false,
      selectedBook: null,
      isConfirmVisible: false,
      bookToDelete: null,
    };
  },
  mounted() {
    this.fetchBooks();
  },
  methods: {
    openAddModal() {
      this.selectedBook = null;
      this.isModalOpen = true;
    },
    openEditModal(book) {
      this.selectedBook = book;
      this.isModalOpen = true;
    },
    openDeleteModal(book) {
      this.bookToDelete = book;
      this.isConfirmVisible = true;
    },
    async fetchBooks() {
      try {
        const response = await axios.get("http://localhost:8000/api/books/");
        this.books = response.data;
      } catch (error) {
        console.error("Error fetching books:", error);
      }
    },
    async deleteBook() {
      try {
        await axios.delete(
          `http://localhost:8000/api/books/${this.bookToDelete.id}/`
        );
        toast.success("Book deleted successfully", { autoClose: 1000 });
        this.isConfirmVisible = false;
        this.bookToDelete = null;
        this.fetchBooks();
      } catch (error) {
        toast.error(error.response?.data?.error || "Failed to delete book", {
          autoClose: 2000,
        });
      }
    },
    handleSaved() {
      this.fetchBooks();
      this.isModalOpen = false;
    },
  },
};
</script>

<style scoped>
/* Table Styling */
table {
  border-spacing: 0;
}

th,
td {
  border-bottom: 2px solid #e0e7ff;
}

th {
  font-size: 14px;
  font-weight: 600;
}

td {
  font-size: 14px;
}

tbody tr:hover {
  background-color: #f1f5f9;
}

tbody tr:nth-child(even) {
  background-color: #fafafa;
}

/* Button Styling */
button {
  transition: background-color 0.2s, transform 0.2s ease-in-out;
}

button:hover {
  transform: scale(1.05);
}

button:active {
  transform: scale(0.98);
}
</style>
