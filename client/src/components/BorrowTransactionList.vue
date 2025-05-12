<template>
  <div class="p-6 bg-gray-50 min-h-screen">
    <div
      class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6 gap-4"
    >
      <h1 class="text-2xl font-bold text-blue-800">📖 Book Transactions</h1>
      <div class="flex gap-3">
        <button
          class="px-4 py-2 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition"
          @click="isBorrowModalOpen = true"
        >
          ➕ Borrow Book
        </button>
        <button
          class="px-4 py-2 rounded-lg bg-green-600 text-white font-semibold hover:bg-green-700 transition"
          @click="isReturnModalOpen = true"
        >
          🔄 Return Book
        </button>
      </div>
    </div>

    <div class="overflow-x-auto shadow-md rounded-lg bg-white">
      <table class="min-w-full table-auto border-collapse">
        <thead class="bg-gradient-to-r from-blue-500 to-blue-700 text-white">
          <tr>
            <th class="py-3 px-6 text-center text-sm font-semibold">
              Borrower Name
            </th>
            <th class="py-3 px-6 text-center text-sm font-semibold">
              Book Title
            </th>
            <th class="py-3 px-6 text-center text-sm font-semibold">Date</th>
            <th class="py-3 px-6 text-center text-sm font-semibold">Status</th>
          </tr>
        </thead>
        <tbody class="text-gray-700">
          <tr
            v-for="transaction in transactions"
            :key="transaction.id"
            class="hover:bg-blue-100 transition duration-200 even:bg-gray-50"
          >
            <td class="py-3 px-6 text-center">
              {{ transaction.user.first_name }} {{ transaction.user.last_name }}
            </td>
            <td class="py-3 px-6 text-center">{{ transaction.book.title }}</td>
            <td class="py-3 px-6 text-center">{{ transaction.date }}</td>
            <td class="py-3 px-6 text-center capitalize">
              <span
                :class="{
                  'text-green-600 font-medium':
                    transaction.status === 'returned',
                  'text-yellow-600 font-medium':
                    transaction.status === 'borrowed',
                }"
              >
                {{ transaction.status }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Borrow Modal -->
    <BorrowFormModal
      :visible="isBorrowModalOpen"
      @close="isBorrowModalOpen = false"
      @saved="fetchTransactions"
    />

    <!-- Return Modal -->
    <ReturnFormModal
      :visible="isReturnModalOpen"
      :transactions="transactions"
      @close="isReturnModalOpen = false"
      @saved="fetchTransactions"
    />
  </div>
</template>

<script>
import axios from "axios";
import BorrowFormModal from "@/components/BorrowFormModal.vue";
import ReturnFormModal from "@/components/ReturnFormModal.vue";

export default {
  name: "BorrowTransactionList",
  components: {
    BorrowFormModal,
    ReturnFormModal,
  },
  data() {
    return {
      transactions: [],
      isBorrowModalOpen: false,
      isReturnModalOpen: false,
    };
  },
  mounted() {
    this.fetchTransactions();
  },
  methods: {
    async fetchTransactions() {
      try {
        const response = await axios.get(
          "http://localhost:8000/api/transactions/"
        );
        this.transactions = response.data.borrow_transactions;
      } catch (error) {
        console.error("Error fetching transactions:", error);
      }
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

/* Modal Styling */
.modal {
  transition: opacity 0.2s ease-in-out;
}

/* Status Styling */
.text-green-600 {
  color: #48bb78;
}

.text-yellow-600 {
  color: #ecc94b;
}
</style>
